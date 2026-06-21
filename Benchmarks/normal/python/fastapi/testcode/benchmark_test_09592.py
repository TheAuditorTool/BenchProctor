# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest09592(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return {"updated": True}
