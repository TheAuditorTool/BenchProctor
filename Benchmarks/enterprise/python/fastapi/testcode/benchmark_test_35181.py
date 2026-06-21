# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest35181(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    def normalize(value):
        return value.strip()
    data = normalize(argv_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
