# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest01036(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    os.remove(str(data))
    return {"updated": True}
