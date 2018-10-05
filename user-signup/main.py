from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route("/validate", methods=['POST'])
def validate_inputs():
    username = request.form['username']
    username_error = ''
    if (username=='' or len(username) < 3 or len(username) > 20):
        username_error = ' Invalid User Name '
    elif (' ' in username) == True:
         username_error = ' Invalid User Name '

    password = request.form['password']
    password_error = ''
    if (password=='' or len(password) < 3 or len(password) > 20):
        password_error = ' Invalid Password '
    elif (' ' in password) == True:
        password_error = ' Invalid password '

    verify_password = request.form['verify']
    verify_password_error = ''    
    if (verify_password != password):
        verify_password_error = ' Password does not match '  

    email = request.form['email']
    email_error = ''
    if (email != ''):   
        if email.count("@") != 1 or email.count(".") != 1: 
            email_error = 'Invalid email '
        elif(  len(email)<3 or len(email) > 20 ): 
            email_error = "Invalid email"   
        elif (' ' in email ) == True:
            email_error = ' Invalid email '


    if (not username_error) and (not password_error) and (not verify_password_error)and (not email_error):
        template = jinja_env.get_template('greeting.html')
        return template.render(name=username)
    else:
        template = jinja_env.get_template('form.html')
        return template.render(username=username,
            username_error=username_error,passsword=password,password_error=password_error,
            verify_passsword=verify_password,verify_password_error=verify_password_error,
            email=email,email_error=email_error)
app.run()

