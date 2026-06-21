# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from starlette.responses import JSONResponse


async def BenchmarkTest57909(request: Request):
    user_id = request.query_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', user_id):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = user_id
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
