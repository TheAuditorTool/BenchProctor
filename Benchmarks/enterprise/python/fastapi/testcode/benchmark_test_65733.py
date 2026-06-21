# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest65733(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return {"updated": True}
