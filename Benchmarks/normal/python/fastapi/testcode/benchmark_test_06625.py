# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest06625(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
