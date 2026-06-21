# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest53624(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
