# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from dataclasses import dataclass
from starlette.responses import JSONResponse
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest08057(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
