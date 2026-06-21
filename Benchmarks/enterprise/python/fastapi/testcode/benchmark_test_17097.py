# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest17097(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
