# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest69155(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
