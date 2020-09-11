from flask import Blueprint,jsonify,request

from .extensions import mongo


main = Blueprint('main',__name__)


@main.route("/")
def route():
    return jsonify({"coffee machine" : "http://127.0.0.1:5000/coffee_machine",
                    "coffee pods":"http://127.0.0.1:5000/coffee_pods"})



@main.route("/coffee_machine",methods=['GET'])
def get_coffe_machine():


    filter = {}
    output = []
    
    product_type = request.args.get('product_type')
    water_line = request.args.get('water_line')
    
    if product_type:
        filter['product_type']=product_type
    if water_line:
        filter['water_line_compatible'] = water_line 
    if filter:
        data = mongo.db.coffee_machine.find(filter)
        print(filter)
        for q in data:
            output.append(q['name'])
        return jsonify(result=output)


    data = mongo.db.coffee_machine
    for q in data.find():
        water_line_compatible = "" if q['water_line_compatible'] =='false' else "water_line_compatible"
        output.append( f"{q['name']} - {q['product_type']}, {q['model']},{water_line_compatible} ")
                          
    return jsonify({'result':output})



@main.route("/coffee_pods",methods=['GET'])
def get_coffee_pods():
    
    
    filter = {}
    output = []
    product_type  = request.args.get('product_type')
    coffee_flavor = request.args.get('coffee_flavor')
    pack_size     = request.args.get('pack_size')
    
    if product_type:
        filter['product_type'] = product_type
    if coffee_flavor:
        filter['coffee_flavor'] = coffee_flavor
    if pack_size:
        filter['pack_size'] = pack_size
    if filter:
        data = mongo.db.coffee_pods.find(filter)
        print(data)
        print(filter)
        for q in data:
            output.append(q['name'])
        return jsonify(result=output)   
        
   
    data = mongo.db.coffee_pods
    for q in data.find():
        output.append(f"{q['name']} - {q['product_type']}, {q['pack_size']}, {q['coffee_flavor']}")
       
    return jsonify({'result':output})