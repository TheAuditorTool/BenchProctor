# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest18597(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = str(argv_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
