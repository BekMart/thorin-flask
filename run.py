import os # standard python library
import json # import json library to import the data because the data is being passed as JSON
from flask import Flask, render_template, request, flash # import the Flask class - tells us where to look for templates/satatic files. render_template function imported. request library imported to find out whatb method we use and to contain form object once posted. flash is to create user feedback
if os.path.exists("env.py"):
    import env # only import env library if the file is found on the system

app = Flask(__name__) # create an instance of class (usually called 'app') / initiate app
app.secret_key = os.environ.get("SECRET_KEY") # this is how we grab our hidden variable


@app.route("/") # @ = decorator / used to tell Flask what URL should trigger the function. ("/") = route directory - so when route directory is browsed - function is triggered
def index():
    return render_template("index.html") # creates template of arguement / save in 'templates' folder which should be on the same level as run.py


@app.route("/about") # when /about is accessed it triggers the following function which brings up the template stored in about.html file
def about():
    data = [] # empty list called data to store data
    with open("data/company.json", "r") as json_data: # need python to open the json file in order to read it (r = read only) and asign it to new variable - json_data
        data = json.load(json_data) # data = parsed json data that we've sent through
    return render_template("about.html", page_title="About", company=data) # comapny is a new variable that will be sent through to HTML template, equal to the list of data its loading from json file


@app.route("/about/<member_name>") # need to create a new route decorator as the other about page is for all members/this will be for individuals
def about_member(member_name): # function takes the arguement of member_name
    member = {} # empty object to store data
    with open("data/company.json", "r") as json_data: # open company.json as a read only file to obtain data
        data = json.load(json_data) # data = information from above file parsed through json
        for obj in data: # iterate through data array just created 
            if obj["url"] == member_name: # if object key = "url" + value = member_name...
                member = obj # fill member variable with member_name
    return render_template("member.html", member=member) # create template using member.html. member name being passed through into member.html = member object created inside function


@app.route("/contact", methods=["GET", "POST"]) # when /contact is accessed it triggers the following function which brings up the template stored in contact.html. Need to add methods=["GET", "POST"] so that route can access these methods
def contact():
    if request.method == "POST": # use this if statment to test to see if the method is working correctly
        # print(request.form) # this prints all of the form contents to the terminal
        # print(request.form.get("name")) # this prints the name value to the temrinal
        # print(request.form["email"]) # this prints the email value to terminal 
        flash("Thanks {}, we have recieved your message!".format(request.form.get("name"))) # generates a flash message giving user feedback that form has been receieved successfully
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__": # __main__" is the name of default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # use module to get "IP" enviroment variable if it exists/otherwise set default to "0.0.0.0"
        port=int(os.environ.get("PORT", "5000")), # use module to get "PORT" enviroment variable if it exists/otherwise set default to "5000" - commonly used in Flask
        debug=True) # allows us to easily dubug our code during development stage - MAKE SURE THIS IS CHANGED TO False WHEN YOU SUBMIT PROJECTS