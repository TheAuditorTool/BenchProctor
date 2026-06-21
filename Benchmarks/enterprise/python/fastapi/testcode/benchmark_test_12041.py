# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import importlib


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest12041(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
