from flask import Flask,jsonify,request,render_template,url_for

app = Flask(__name__)

orders = [
    {"id":1,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":2,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":3,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":4,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":5,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"},
    {"id":6,"No of items ordered":1,"name":"pizza","cost":123,"status":"pending"}
]

@app.route("/",methods=['GET'])
def index():
    return jsonify({"message":"It works well"})
    # return render_template()

@app.route("/orders",methods=['GET'])
def returnAllOrders():
    orders
    return render_template("customer.html",orders = orders)

@app.route("/orders/<int:id>")
def returnOne(id):
    global orders
    specific_order = [order for order in orders if order["id"] == id]
    orders = specific_order
    return render_template("customer.html", orders = orders)
@app.route("/orders",methods=['POST'])
def addOrders():
    if request.method == 'POST':
        result = request.form 
        orders.append(result)
    return render_template('customer.html',orders)
if __name__ == "__main__":
    app.run(debug=True)
