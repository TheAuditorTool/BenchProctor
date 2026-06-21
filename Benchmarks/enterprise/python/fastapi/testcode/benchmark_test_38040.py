# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from types import SimpleNamespace


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest38040(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    request.session['data'] = str(data)
    return {"updated": True}
