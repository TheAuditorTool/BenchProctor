# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from dataclasses import dataclass
from starlette.responses import JSONResponse
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09217(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
