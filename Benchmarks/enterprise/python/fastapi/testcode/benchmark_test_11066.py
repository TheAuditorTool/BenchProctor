# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest11066(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
