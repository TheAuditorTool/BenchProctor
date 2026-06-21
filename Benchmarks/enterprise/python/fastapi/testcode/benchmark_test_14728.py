# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest14728(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = relay_value(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}
