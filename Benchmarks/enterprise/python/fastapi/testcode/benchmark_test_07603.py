# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import os


async def BenchmarkTest07603(request: Request, field: str = Form('')):
    field_value = field
    prefix = ''
    data = prefix + str(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
