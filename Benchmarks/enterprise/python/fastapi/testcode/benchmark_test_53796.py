# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest53796(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
