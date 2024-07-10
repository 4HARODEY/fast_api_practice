from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='First_APP'
)


users_db = [
    {'id': 1, 'name': 'Roman', 'role': 'admin'},
    {'id': 2, 'name': 'Anton', 'role': 'sys_admin'},
    {'id': 3, 'name': 'Vova', 'role': 'user'},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users/{user_id}")
async def user_info(user_id: int):
    return [user for user in users_db if user.get("id") == user_id]


@app.post("/users/{user_id}")
async def user_info(user_id: int, new_name: str):
    cur_user = users_db[user_id]
    cur_user["name"] = new_name
    return {'status': 'success', 'data': cur_user}


trade_db = [
    {'trade_id': 1222, 'user_id': 1, 'currency': 'USD', 'amount': 2.13},
    {'trade_id': 1223, 'user_id': 3, 'currency': 'BTC', 'amount': 22.13},
    {'trade_id': 1224, 'user_id': 2, 'currency': 'BTC', 'amount': 10.13},
]


class Trade(BaseModel):
    trade_id: int
    user_id: int
    currency: str
    amount: float


@app.post("/trades")
async def add_trades(trades: list[Trade]):
    trade_db.extend(trades)
    return {'status': 'success', 'data': trade_db}
