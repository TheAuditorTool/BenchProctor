# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest09775(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
