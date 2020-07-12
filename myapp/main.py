from flask import Flask, request
import boto3
import json

db = boto3.resource('dynamodb')

app = Flask(__name__)

# add a rule for the index page.
@app.route("/")
def hello():
    return "HELLO WE DEPLOYED"


@app.route("/cued", methods=["POST"])
def post_cued():
    data = json.loads(request.data)

    for key in data:
        data[key] = str(data[key])
    table = db.Table('Cued')

    response = table.put_item(
        Item=data
    )
    return response

@app.route("/cued/<cued_id>/issue/<issue_id>")
def get_cued(cued_id, issue_id):

    table = db.Table('Cued')
    print(cued_id, issue_id)
    #response = table.get_item(Key={'CueId': "oregon-medicaid-benefits", 'IssueId': "12341234"})

    response = table.get_item(Key={'CueId': str(cued_id), 'IssueId': str(issue_id)})
    return response


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
