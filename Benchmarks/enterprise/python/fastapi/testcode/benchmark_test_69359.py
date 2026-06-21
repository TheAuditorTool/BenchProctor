# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest69359(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    yaml.safe_load(data)
    return {"updated": True}
