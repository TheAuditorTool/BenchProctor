# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest00774(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
