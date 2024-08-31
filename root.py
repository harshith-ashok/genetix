from flask import Flask, redirect, render_template
import mysql.connector as sql
import data
import random

app = Flask(__name__)

# Establishing Connection
con = sql.connect(user='root', password='P@ss4SQl',
                  host='localhost', auth_plugin='mysql_native_password')
cur = con.cursor()
cur.execute('use gen_alg')


@app.route("/")
def root():
    cur.execute('SELECT * FROM master;')
    master_data = cur.fetchall()
    cur.execute(
        "select * from master where(eye,height,ear,hair)=('D','D','D','D');")
    per_data = cur.fetchall()
    cur.execute(
        "select * from master where(eye,height,ear,hair)=('R','R','R','R');")
    res_data = cur.fetchall()
    cur.execute("SELECT COUNT(hair) AS CNT FROM master WHERE hair='D'")
    hair = cur.fetchall()
    cur.execute("SELECT COUNT(eye) AS CNT FROM master WHERE eye='D'")
    height = cur.fetchall()
    cur.execute("SELECT COUNT(ear) AS CNT FROM master WHERE ear='D'")
    eye = cur.fetchall()
    cur.execute("SELECT COUNT(height) AS CNT FROM master WHERE height='D'")
    ear = cur.fetchall()
    cat_L = [hair, height, eye, ear]
    return render_template('root.html', master_data=master_data, per_data=per_data, res_data=res_data, cat_L=cat_L)


@app.route("/reset")
def resetData():
    cur.execute('DROP TABLE master;')
    cur.execute('CREATE TABLE master(sno int primary key auto_increment, name varchar(255), hair varchar(20),height varchar(20),ear varchar(20),eye varchar(20));')
    for i in range(len(data.names)):
        hei_trait = data.traits[random.randint(0, 1)]
        hai_trait = data.traits[random.randint(0, 1)]
        eye_trait = data.traits[random.randint(0, 1)]
        ear_trait = data.traits[random.randint(0, 1)]
        cur.execute("INSERT INTO master(name,hair,eye,ear,height) VALUES('{name}','{hei_trait}','{hai_trait}','{eye_trait}','{ear_trait}')".format(
            name=data.names[i], hei_trait=hei_trait, hai_trait=hai_trait, eye_trait=eye_trait, ear_trait=ear_trait,))
    con.commit()
    print(cur.rowcount, "record(s) affected")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
