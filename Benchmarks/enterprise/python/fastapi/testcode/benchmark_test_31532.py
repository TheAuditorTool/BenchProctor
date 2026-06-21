# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest31532(request: Request, field: str = Form('')):
    field_value = field
    prefix = ''
    data = prefix + str(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
