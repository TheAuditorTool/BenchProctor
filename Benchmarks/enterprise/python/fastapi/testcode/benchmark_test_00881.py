# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest00881(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
