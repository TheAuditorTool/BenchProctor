# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import json
from starlette.responses import JSONResponse


async def BenchmarkTest73281(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
