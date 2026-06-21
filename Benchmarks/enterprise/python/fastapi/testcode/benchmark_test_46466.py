# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest46466(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    os.environ['APP_USER_PREFERENCE'] = str(xml_value)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
