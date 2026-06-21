# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from types import SimpleNamespace
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest13942(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
