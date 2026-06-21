# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest11528(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
