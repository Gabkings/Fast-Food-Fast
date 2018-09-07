from flask import Flask,jsonify,request,render_template,url_for

# app = Flask(__name__)
app = Flask(__name__, template_folder='{}/templates'.format(app_path), static_folder='{}/static'.format(app_path))

orders = [
    # {"id":1,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    # {"id":2,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    # {"id":3,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    # {"id":4,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    # {"id":5,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    # {"id":6,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"}
]

@app.route("/",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/orders",methods=['GET'])
def returnAllOrders():
    # return jsonify({'Orders':orders})
    return render_template()

@app.route("/orders/<int:id>")
def returnOne(id):
    specific_order = [order for order in orders if order["id"] == id]
    return jsonify({"Oder":specific_order[0]})

@app.route("/orders",methods=['POST'])
def addOrders():
    #specific_order = {"id":request.json['id'],"No of items ordered":1,"name":request.json['name'],"cost":request.json['cost'],"date":"11/22/018","status":"pending"} 
    if request.method == 'POST':
        result = request.form 
        orders.append(result)
    return jsonify({"orders":orders})
@app.route("/orders/<int:id>",methods=['PUT'])
def updateOne(id):
    specific_order = [order for order in orders if order["id"] == id]

if __name__ == "__main__":
    app.run(debug=True)
