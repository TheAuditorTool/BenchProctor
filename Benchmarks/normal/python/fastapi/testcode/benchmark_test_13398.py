# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest13398(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
