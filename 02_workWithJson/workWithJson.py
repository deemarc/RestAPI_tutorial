from flask import Flask, jsonify
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

if __name__ =="__main__":
    app.run()