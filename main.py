from fastapi import FastAPI, Response, status
import random
app = FastAPI()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

domain = "a.com"
exist = []
newList = []
idList = []
urlList = []

def idCreate( exist:list):
    while True:
        id = "{0:04}".format(random.randint(0,9999))
        try:
            exist.index(id)
        except(ValueError):
            break
        else:
            pass
        
    exist.append(id)

    if len(exist) >= 1000:
        for i in range(800,1000):
            newList.append(exist[i])
        exist.clear()
        for i in newList:
            exist.append(i)
        newList.clear()

    return id

@app.get("/")
async def link(link:str):
    id = idCreate(exist)
    if len(idList) < 1000:
        idList.append(id )
        urlList.append(link)
    else:
        idList.pop(0)
        idList.append(id)
        urlList.pop(0)
        urlList.append(link)

    if link[0:5]=="http:":
        return "http://" + domain + "/r/" +id
    elif link[0:5]=="https":
        return "http://" + domain + "/r/" +id
    else:
        return "PROC_INVALID"
        
@app.get("/r/")
async def r(id:str):
    try:
        idindex = idList.index(id)
    except(ValueError):
        return "ID_NOT_EXIST"
    else:
        return urlList[idindex]