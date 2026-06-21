# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest20261(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
