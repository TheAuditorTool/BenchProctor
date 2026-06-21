# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from starlette.responses import JSONResponse


async def BenchmarkTest30460(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
