####################################################################
#   mongo DB and REST API with endpoints that return the JSON data #
#          for the coffee machines and coffee pods                 #
####################################################################
from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# connecting to database named 'database' installed locally
app.config['MONGO_DBNAME'] = 'databasename'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/database'

mongo = PyMongo(app)

#######################################
# endpoint to find any machine or pod #
#######################################
# usage: 
# All large machines    => http://localhost:5000/my_gfg_collection/COFFEE_MACHINE_LARGE
# All espresso machines => http://localhost:5000/my_gfg_collection/ESPRESSO_MACHINE
# All large pods        => http://localhost:5000/my_gfg_collection/COFFEE_POD_LARGE
# All small pods        => http://localhost:5000/my_gfg_collection/COFFEE_POD_SMALL
#######################################
@app.route('/my_gfg_collection/<name>', methods=['GET'])
def get_all_large_machines_pods(name):
    product = mongo.db.my_gfg_collection 

    output = []

    for q in product.find():
        if(q['product type'] == name):
            output.append({'code' : q['code']})

    return jsonify({'result' : output})

##############################################
# endpoint to find All espresso vanilla pods #
##############################################
# usage: 
# All espresso vanilla pods => http://localhost:5000/my_gfg_collection/ESPRESSO_POD/vanilla
#######################################
@app.route('/my_gfg_collection/ESPRESSO_POD/<name>', methods=['GET'])
def get_all_espresso_pods(name):
    product = mongo.db.my_gfg_collection 

    output = []
    
    for q in product.find():
        if(q['product type'] == 'ESPRESSO_POD' and q['coffee_flavor'] == name):
            output.append({'code' : q['code']})

    return jsonify({'result' : output})

###################################################      
# endpoint to find All pods sold in 7 dozen packs #
################################################### 
# usage: 
# All pods sold in 7 dozen => http://localhost:5000/my_gfg_collection/POD/7
#######################################
@app.route('/my_gfg_collection/POD/<name>', methods=['GET'])
def get_all_pods_7packs(name):
    product = mongo.db.my_gfg_collection 

    output = []
    
    # using explicit type casting. string to int so that we can compare numbers
    for q in product.find():
        if(q['pack_size'] == int(name)):
            output.append({'code' : q['code']})

    return jsonify({'result' : output})

############################ 


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)