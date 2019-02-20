from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/helloJson')
def hello_Json():
    jsonData = {
        "field1_str":"value1",
        "field2_boolean": True,
        "field3_json":
            {
                "f3_field1_str":"subJson"
            }
    }
    return jsonify(jsonData)

@app.route('/heyJson_addThisTwoNumber',methods=['POST'])
def addTwoNumber():
    print(request.url)
    isJson = request.is_json
    print(request.is_json)
    if not(request.is_json):
        return "the request parameter is not json"
        
    dataDict = request.get_json()

    a = dataDict["a"]
    b = dataDict["b"]
    dataDict["result"] = a + b


    return jsonify(dataDict)

if __name__ =="__main__":
    app.run(debug=True)