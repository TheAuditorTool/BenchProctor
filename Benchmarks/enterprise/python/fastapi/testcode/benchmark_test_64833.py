# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from starlette.responses import JSONResponse


async def BenchmarkTest64833(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = ua_value
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
