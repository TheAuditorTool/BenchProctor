# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest03442(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if env_value not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + env_value
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
