# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest07919(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
