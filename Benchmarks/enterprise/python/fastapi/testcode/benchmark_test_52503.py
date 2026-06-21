# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest52503(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
