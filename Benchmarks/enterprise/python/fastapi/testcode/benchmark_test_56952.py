# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest56952(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return {"updated": True}
