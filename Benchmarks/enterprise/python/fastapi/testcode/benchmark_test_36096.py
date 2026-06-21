# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest36096(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = dotenv_value if dotenv_value else 'default'
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
