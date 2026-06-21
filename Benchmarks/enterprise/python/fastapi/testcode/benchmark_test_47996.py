# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest47996(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return {"updated": True}
