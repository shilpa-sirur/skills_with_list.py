from flask import Flask, request, render_template, redirect, flash
import os

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'



@app.route("/")
def start_here():
	return render_template("application-form.html")


@app.route("/search", methods=["POST"])
def go_here():
	Firstname = request.form.get("firstname")
	Lastname = request.form.get("lastname")
	Salary = request.form.get("salary")
	Job = request.form.get("job")
	
	if not Firstname or not Lastname or not Salary or not Job :
    		flash("please type all the information")
   	else:
    		return render_template("application.html", Firstname=Firstname, Lastname= Lastname, Salary = Salary, Job=Job )
    
    	return(redirect(request.referrer))











	 	












	


	









if __name__ == "__main__":
    app.run(debug=True)
