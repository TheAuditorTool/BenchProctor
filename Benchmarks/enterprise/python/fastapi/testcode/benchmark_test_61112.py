# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest61112(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
