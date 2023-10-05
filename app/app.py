from flask import*
from flask import render_template
import mysql.connector
import os


app = Flask(__name__, static_folder="assets", template_folder="templates")

myconn = mysql.connector.connect(host = os.environ["DB_HOST"], user = "root",password = "root",database = "db", port = "3306")
curr = myconn.cursor()


@app.route("/")
def k():
	return render_template("index.html")

@app.route("/<a>")
def k1(a):
	t=a+".html"
	return render_template(t)

@app.route("/submit",methods=["POST"])
def k2():
	k="\n\nEmail: "+request.form["email"]+"\nName: "+request.form["name"]+"\nPhone number: "+request.form["phone"]+"\nMessage: "+request.form["message"]
	print(k)
	name = request.form["name"]
	email = request.form['email']
	phonenumber = request.form['phone']
	message = request.form['message']
	try:
		insert_stmt = (
   "INSERT INTO INFO(_NAME, _EMAIL, _PHONENUMBER, _MESSAGE)"
   "VALUES (%s, %s, %s, %s)")
		data = (name,email,phonenumber,message)
		curr.execute(insert_stmt,data)
		myconn.commit()
	except:
		print("Error Occured")
	
	return render_template("contact.html")

# @app.errorhandler(404)
# def k3():
# 	return render_template("err.html")

# @app.errorhandler(Exception)
# def k4(Exception):
# 	return render_template("err_5.html")

# @app.route("/")
# def homePage():
# 	return "<h1>Hello World</h1>"

if __name__ == '__main__':
	app.run(host = "0.0.0.0",port = 5000)
# 	app.run(debug = True)
