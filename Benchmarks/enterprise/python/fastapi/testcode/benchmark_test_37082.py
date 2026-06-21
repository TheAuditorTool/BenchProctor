# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest37082(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(dotenv_value), max_age=86400)
    return resp
