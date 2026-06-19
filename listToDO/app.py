from flask import Flask,url_for,redirect,request,jsonify
import mysql.connector

app = Flask(__name__)

def mysql_connection():
    return mysql.connector.connect(
        host="",
        username="",
        password="",
        database="listtodo"
    )


@app.route("/")
def main():
    return app.send_static_file('index.html')

@app.route('/add-task',methods=["POST"])
def add_task():
    db = mysql_connection()
    curr = db.cursor()

    data = request.values.get("add-task-content")

    query = "insert into tasks (task_content) values (%s);"
    curr.execute(query,(data,))

    # I forget it 
    db.commit()

    curr.close()
    db.close()

    return redirect(url_for('main'))


@app.route('/rm-tasks',methods=["POST"])
def remove_tasks():
    if request.method == "POST":
        db = mysql_connection()
        curr = db.cursor()

        query = "delete from tasks"
        curr.execute(query)
        db.commit()

        db.close()
        curr.close()
        
        return redirect(url_for('main'))

@app.route('/all-tasks',methods=["GET"])
def fetch_tasks():
    db = mysql_connection()
    curr = db.cursor(dictionary=True)

    query = "select * from tasks"
    curr.execute(query)
    data = curr.fetchall()

    curr.close()
    db.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)