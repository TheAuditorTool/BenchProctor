# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest12759(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    eval(str(data))
    return {"updated": True}
