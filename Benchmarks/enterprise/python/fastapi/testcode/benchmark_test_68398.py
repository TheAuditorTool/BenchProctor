# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest68398(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
