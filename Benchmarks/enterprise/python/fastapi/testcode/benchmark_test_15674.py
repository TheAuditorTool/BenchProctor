# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest15674(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
