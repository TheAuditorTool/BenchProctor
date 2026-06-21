# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest49408(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
