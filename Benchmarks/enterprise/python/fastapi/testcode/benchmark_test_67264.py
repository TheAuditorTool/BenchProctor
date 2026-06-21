# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from starlette.responses import JSONResponse


async def BenchmarkTest67264(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = user_id
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
