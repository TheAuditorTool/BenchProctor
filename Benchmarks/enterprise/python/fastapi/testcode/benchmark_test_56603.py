# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest56603(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = default_blank(dotenv_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
