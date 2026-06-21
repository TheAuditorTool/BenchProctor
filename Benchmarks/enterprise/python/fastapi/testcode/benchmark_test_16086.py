# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest16086(request: Request):
    path_value = request.path_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
