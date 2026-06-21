# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest54889(request: Request):
    host_value = request.headers.get('host', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if host_value not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + host_value
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
