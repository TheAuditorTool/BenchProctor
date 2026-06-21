# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest58402(request: Request, req: UserInput):
    json_value = req.payload
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    yaml.safe_load(data)
    return {"updated": True}
