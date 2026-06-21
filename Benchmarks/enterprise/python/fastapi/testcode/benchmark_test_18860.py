# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18860(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
