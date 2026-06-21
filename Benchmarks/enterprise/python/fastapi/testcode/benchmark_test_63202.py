# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest63202(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = argv_value if argv_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
