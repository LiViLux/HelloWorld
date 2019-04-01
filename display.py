from flask import Flask, render_template, request

import mysql.connector as mariadb

app = Flask (__name__)

@app.route('/')

def lists():
    conn=mariadb.connect(user='lividatadb1', password='dojaja', database='lividatadb1')
    cur=conn.cursor()
    cur.execute("select * from Table1")
    rows=cur.fetchall()
    return render_template("display.html", rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
