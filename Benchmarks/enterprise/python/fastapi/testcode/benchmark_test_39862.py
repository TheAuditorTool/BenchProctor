# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import json


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest39862(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
