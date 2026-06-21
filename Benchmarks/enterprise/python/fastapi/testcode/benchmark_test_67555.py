# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest67555(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
