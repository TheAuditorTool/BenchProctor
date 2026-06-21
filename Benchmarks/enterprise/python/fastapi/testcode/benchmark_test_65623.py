# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest65623(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    auth_check('user', data)
    return {"updated": True}
