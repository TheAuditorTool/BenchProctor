# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from app_runtime import db, User


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest52022(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
