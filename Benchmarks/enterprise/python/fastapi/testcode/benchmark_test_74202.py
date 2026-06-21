# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest74202(request: Request, req: UserInput):
    json_value = req.payload
    data, _sep, _rest = str(json_value).partition('\x00')
    yaml.safe_load(data)
    return {"updated": True}
