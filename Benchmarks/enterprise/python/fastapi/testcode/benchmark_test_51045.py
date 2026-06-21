# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from fastapi import Form
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest51045(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
