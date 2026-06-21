# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import importlib


def relay_value(value):
    return value

async def BenchmarkTest01078(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
