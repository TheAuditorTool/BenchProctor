# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse
import subprocess


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01858(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
