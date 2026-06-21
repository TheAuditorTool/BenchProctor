# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest29668(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
