# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest10716(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
