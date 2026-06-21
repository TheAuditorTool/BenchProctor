# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest79075(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
