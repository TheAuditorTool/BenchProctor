# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
from starlette.responses import JSONResponse
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02130(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
