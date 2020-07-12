from flask import Flask
import boto3

db = boto3.resource('dynamodb')

app = Flask(__name__)

# add a rule for the index page.
@app.route("/")
def hello():
    return "HELLO WE DEPLOYED"

@app.route("/dbhit")
def dbhit():
    table = db.Table('Cued')
    response = table.get_item(Key={'CueId': "oregon-medicaid-benefits", 'IssueId': "12341234"})
    return response

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
