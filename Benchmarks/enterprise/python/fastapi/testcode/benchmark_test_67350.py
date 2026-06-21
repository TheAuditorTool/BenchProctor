# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db, User


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest67350(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
