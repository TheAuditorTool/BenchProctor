# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest60630(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    request.session['user'] = str(processed)
    return {"updated": True}
