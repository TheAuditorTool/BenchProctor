# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest11981(request: Request):
    referer_value = request.headers.get('referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
