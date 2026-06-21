# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import json


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72634(request: Request, req: UserInput):
    json_value = req.payload
    json.loads(json_value)
    return {"updated": True}
