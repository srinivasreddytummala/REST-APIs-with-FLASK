from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'My Store',
        'items':[
            {
                'name':'soap',
                'cost':'$12.34'
        }
        ]
    }
]

@app.route('/')
def hello():
    return "HELLO WORLD"


# create a store
@app.route('/store/', methods = ['POST'])
def create_store():
    print("_______________request___________________")
    print(request)
    request_data =  request.get_json()
    print("____________request_data___________________")
    print(request_data)
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)

    return jsonify(new_store)

    


# get particular store
@app.route('/store/<string:storename>/')
def get_store(storename):

    for store in stores:
        if store["name"] == storename:
            return jsonify(store)
    return jsonify({'mesage':'store not found'})        
    


# get all the available stores
@app.route('/store/')
def get_stores():
    
    return jsonify({'stores':stores})



@app.route('/store/<string:storename>/item/', methods = ['POST'])
def create_item_in_store(storename):
    
    request_data = request.get_json()
    for store in stores:
        if store["name"] == storename:

            new_item = {
                'name': 'Shirt',
                'cost': '$122.23'
            }

            store["items"].append(new_item)

            return jsonify(new_item)
    return jsonify({"message":"store not found"})


# get the items in a store
@app.route('/store/<string:storename>/item/')
def get_item_in_store(storename):

    for store in stores:
        if store["name"] == storename:
            return jsonify({"items":store['items']})

    return jsonify({"mesage":"store not found"})        
    


app.run(port = 5000)


