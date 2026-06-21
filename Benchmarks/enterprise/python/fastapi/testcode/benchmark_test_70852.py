# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import json
import os


async def BenchmarkTest70852(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
