from flask import Flask, jsonify, request
from flask_restful import Api, Resource

#some flask and flask restful initialize process
app = Flask(__name__)
api = Api(app)

#constant value (not really have in python)
retKey = ["return","statusCode"]
statusCode = {"OK":200,"MissingParam":301, "wrongDataType":302, "DividerZero":303}

#some common function
def errorResponse(errorKey):
    dictData = {
            retKey[0]: "Error Message",
            retKey[1]: statusCode[errorKey]
            }
    return jsonify(dictData)

def passResponse(retVal):
    dictData = {
            retKey[0]: retVal,
            retKey[1]: statusCode["OK"]
            }
    return jsonify(dictData)

#addition function
def checkPalindrome(inStr):
    head = 0
    tail = len(inStr) -1
    isPalin = True
    while(head<tail):
        if inStr[head] == " ":
            head += 1
            continue
        if inStr[tail] == " ":
            tail -= 1
            continue
        if inStr[head] != inStr[tail]:
            isPalin = False
            break
        head += 1
        tail -= 1
        
    return isPalin
#all the resource

class hello_world(Resource):
    def get(self):
        #resource hello_world is requested using method GET
        return passResponse("hello world")

class addTwoNumber(Resource):
    def post(self):
        #resource addTwoNumber is requested using method POST

        #Get posted data:
        postedData = request.get_json()

        #check for input parameters validity
        if "a" not in postedData or "b" not in postedData:
            return errorResponse("MissingParam")
        
        #calculate and return response
        y = postedData["a"] + postedData["b"]
        return passResponse(y)

class sumAll(Resource):
    def post(self):
        postedData = request.get_json()
        if "a" not in postedData:
            return errorResponse("MissingParam")
        
        if type(postedData["a"]) != list:
            return errorResponse("wrongDataType")

        y = sum(postedData["a"])
        return passResponse(y)

class isPalindrome(Resource):
    def post(self):
        postedData = request.get_json()
        if "inString" not in postedData:
            return errorResponse("MissingParam")
        
        if not isinstance(postedData["inString"],str):
            return errorResponse("wrongDataType")
        y = checkPalindrome(postedData["inString"])
        
        return passResponse(y)

class divideTwoNum(Resource):
    def post(self):
        postedData = request.get_json()
        if "a" not in postedData or "b" not in postedData:
            return errorResponse("MissingParam")
        if postedData["b"] == 0:
            return errorResponse("DividerZero")
        
        #calculate and return response
        y = postedData["a"]/postedData["b"]
        return passResponse(y)

api.add_resource(hello_world, "/")
api.add_resource(addTwoNumber, "/addTwoNumber")
api.add_resource(sumAll, "/sumAll")
api.add_resource(isPalindrome, "/isPalindrome")
api.add_resource(divideTwoNum, "/divideTwoNum")

if __name__ =="__main__":
    app.run(debug=True)