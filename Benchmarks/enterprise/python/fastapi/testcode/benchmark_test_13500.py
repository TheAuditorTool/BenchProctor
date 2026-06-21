# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest13500(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
