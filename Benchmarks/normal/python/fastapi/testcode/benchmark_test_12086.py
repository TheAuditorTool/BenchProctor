# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest12086(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    values = str(processed).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
