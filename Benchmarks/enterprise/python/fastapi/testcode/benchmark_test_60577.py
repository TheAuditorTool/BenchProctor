# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import importlib
import sys


class UserInput(BaseModel):
    payload: str = ''
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest60577(request: Request, req: UserInput):
    json_value = req.payload
    ctx = RequestContext(json_value)
    data = ctx.payload
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
