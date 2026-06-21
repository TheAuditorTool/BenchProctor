# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest63215(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % (dotenv_value,)
    request.session.clear()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
