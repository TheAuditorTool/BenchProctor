# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest69484(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % (dotenv_value,)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
