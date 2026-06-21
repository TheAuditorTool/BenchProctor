# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest17269(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return {"updated": True}
