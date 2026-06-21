# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest51945(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
