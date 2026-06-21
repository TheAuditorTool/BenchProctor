# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest17121(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
