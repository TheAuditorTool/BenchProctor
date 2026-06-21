# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest31119(request: Request, req: UserInput):
    json_value = req.payload
    ctx = RequestContext(json_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
