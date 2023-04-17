from flask import Flask,jsonify,request
from products import products
app=Flask(__name__)

@app.route("/ping",methods=['GET'])
def ping():
    return jsonify({
        "message":'pong',
    })
@app.route("/products",methods=['GET'])
def get_products():
    return jsonify({
        "products":products
    })

@app.route("/products/<string:product_name>",methods=['GET'])
def get_product(product_name:str):
    product_found=[product for product in products if product['name']==product_name]
    if(len(product_found)>0):
        return jsonify(product_found[0])
    else:
        return jsonify({
            "message":"product not found"
        })
    
@app.route('/products',methods=['POST'])
def add_product():
    #print(request.json['hello'])
    new_product={
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    products.append(new_product)
    return jsonify({
        "message":"Product Added Successfully",
        "product":new_product
    })


@app.route("/products/<string:product_name>",methods=['PUT'])
def update_product(product_name:str):
    product_found=[product for product in products if product['name']==product_name]
    if (len(product_found)>0):
        product_found[0]['name']=request.json['name'] if len(request.json['name'])>0 else product_found[0]['name']
        product_found[0]['price']=request.json['price'] if len(request.json['price'])>0 else product_found[0]['price']
        product_found[0]['quantity']=request.json['quantity'] if len(request.json['quantity'])>0 else product_found[0]['quantity']
        return jsonify(product_found[0])
    else:
        return jsonify({"message":"product not found"})

@app.route("/products/<string:product_name>",methods=['DELETE'])
def delete_product(product_name:str):
    product_found=[product for product in products if product['name']==product_name]
    if(len(product_found[0])>0):
        products.remove(product_found[0])
        return jsonify(product_found)
    else:
        return jsonify({"message":"product not found"})

if __name__== '__main__':
    app.run(debug=True,port=4000)
