# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest44368(request: Request, req: UserInput):
    json_value = req.payload
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
