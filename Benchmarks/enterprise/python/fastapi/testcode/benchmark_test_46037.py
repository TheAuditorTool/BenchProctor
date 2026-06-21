# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest46037(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
