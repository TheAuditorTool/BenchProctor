# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import os


async def BenchmarkTest55431(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
