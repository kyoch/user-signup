from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)

app.config['DEBUG'] = True      


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/", methods = ['POST'])
def validate():
    username = request.form['username']
    pwd = request.form['pwd']
    v_pwd = request.form['v_pwd']
    email = request.form['email']

    name_error = ''
    pwd_error = ''
    v_pwd_error = ''
    email_error = ''


    if username.strip() == "":
       name_error = "That's not a valid username."
       
    elif len(username) < 3 or len(username) > 20:
       name_error = "That's not a valid username."
        
    elif " " in username:
       name_error = "That's not a valid username."  


    
    if len(pwd) == 0:
       pwd_error = "That's not a valid password."

    if pwd.strip() == "":
       pwd_error = "That's not a valid password." 
    
    elif len(pwd) < 3  or len(pwd) > 20:
       pwd_error = "That's not a valid password."
 
       
  
    if v_pwd != pwd:
       v_pwd_error = "Passwords do not match."
       
  
    if len(email) != 0:
       if "@" not in email:
           email_error = "Invalid Email"
    
       elif "." not in email:
           email_error = "Invalid Email"

       elif " " in email:
           email_error = "Invalid Email"   

       elif len(email) < 3 or len(email) > 20:
           email_error = "Invalid Email"  
        
   
    if len(name_error) == 0 and len(pwd_error) == 0 and len(v_pwd_error) == 0 and len(email_error) == 0:     
        return render_template("welcome.html", username = username)

    else:
        return render_template('index.html', username=username, email=email,name_error=name_error,pwd_error=pwd_error,v_pwd_error=v_pwd_error, email_error=email_error)

'''@app.route("/")
def index():
    
    

    name_error = request.args.get("name_error")
    pwd_error = request.args.get("pwd_error")
    email_error = request.args.get("email_error")

    return render_template('index.html', username=username, pwd=pwd, email=email,name_error=name_error,pwd_error=pwd_error, email_error=email_error)
'''

app.run()    