import json
from bson import ObjectId
from db.db import client1
import  pandas as pd

def postAPI(request_json):
    print(request_json)
    return {"response": request_json}

def getAPI():
    sum = 1+2


    
    return {'sendData':sum}

def GetCustomerData():
    converDb = client1['test']
    convCol = converDb['customer']

    conversionData = pd.DataFrame(convCol.find({}))

    ##convert the datafraame into json
    conversionData = json.loads(conversionData.to_json(orient='records',default_handler=str))
    return conversionData

def customerInfo(data):
    converDb = client1['test']
    convCol = converDb['customer']

    conversionData = pd.DataFrame(convCol.find({"_id":ObjectId(data['user_id'])}))

    ##convert the datafraame into json
    conversionData = json.loads(conversionData.to_json(orient='records',default_handler=str))
    return conversionData

def InsertCustomerInfo(req):
    converDb = client1['test']
    convCol = converDb['customer']
    userCheck = pd.DataFrame(convCol.find({"email":req['email']}))

    if len(userCheck) == 0:
        obj = {
            "first": req['first_name'],
            "last": req['last_name'],
            "name": req['first_name']+" "+req['last_name'],
            "email": req['email'],
            "mob": req['phone'],
            "pass": req['password'],
            "del": 0
        }
        result = convCol.insert_one(obj)
        id = result
        msg = "user inserted sucessfully"
        statuscode = 200
    else:
        msg = "user already exist"
        statuscode = 501

    return {'msg':msg,"statuscode":statuscode,'req':req}