# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import json
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest09571(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    auth_check('user', data)
    return {"updated": True}
