# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import base64
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest78948(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
