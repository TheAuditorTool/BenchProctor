# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest79812(request: Request, req: UserInput):
    json_value = req.payload
    data = handle(json_value)
    processed = data[:64]
    db.execute('DELETE FROM accounts WHERE id = ?', (str(processed),))
    return {"updated": True}
