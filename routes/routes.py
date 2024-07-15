from fastapi import APIRouter, Request
from models.model import postAPI ,getAPI ,GetCustomerData,InsertCustomerInfo,customerInfo

routes = APIRouter()

@routes.get("/getRequest")
async def sendRe():
    return getAPI()

@routes.post("/Post")
async def getReq(request: Request):
    request_json = await request.json()
    result =  postAPI(request_json)
    return result

@routes.get("/cusData")
async def dbCon():
    return GetCustomerData()

@routes.post("/insert")
async def ins(request:Request):
    request_json = await request.json()
    return InsertCustomerInfo(request_json)

@routes.post("/custome_info")
async def ins(request:Request):
    request_json = await request.json()
    return customerInfo(request_json)

