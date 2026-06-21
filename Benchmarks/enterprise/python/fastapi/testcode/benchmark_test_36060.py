# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest36060(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
