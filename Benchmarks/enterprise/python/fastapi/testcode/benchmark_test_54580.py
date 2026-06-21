# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest54580(request: Request):
    ua_value = request.headers.get('user-agent', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, ua_value))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
