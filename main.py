from typing import Optional
from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    element: str

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/sum1n/{number}")
async def sum_to_n(number: int):
    sum = 0
    for i in range(1, number + 1):
        sum = sum + i
    return {"result": sum}

@app.get("/fibo")
def fibo(n: int):

    n1, n2 = 1, 1
    i = 0
    while i < n - 2:
        next = n1 + n2
        n1 = n2
        n2 = next
        i = i + 1
    return {"result": n2}


@app.post("/reverse")
def reverse(word: str = Header(None)):
    return{"result": word[:: -1]}



names = []
elements = []
@app.put("/list")
async def update_list(item: Item):
    elements.append(item.element)
    return {"result": elements}


@app.post("/list")
def checkel(name: str):
        for i in range(0,len(elements)):
            if elements[i] == name:
                return {"error": "it exist"}
            return{"good": "now append"}



@app.get("/even/{num}")
def even_nums(num: int):
    evennum = []
    for i in range(0, num+1):
        if i%2 == 0:
            evennum.append(i)
    return{"result": evennum}




@app.post("/calculator")
async def calculator(calculator: str):
    arr = calculator.split(',')
    num1 = int(arr[0])
    num2 = int(arr[2])
    op = arr[1]
    result = -1
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = int(num1 / num2)
    else:
        result = 0

    return {"result": result}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = "test"):
    # select item_id,name from item where item_id = item_id
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}


