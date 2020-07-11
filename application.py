from flask import Flask

app = Flask(__name__)

# add a rule for the index page.
@app.route("/")
def hello():
    return "HELLO WE DEPLOYED"

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(host="0.0.0.0", port=8000)