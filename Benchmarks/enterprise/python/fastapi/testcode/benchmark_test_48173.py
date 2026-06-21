# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from starlette.responses import HTMLResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest48173(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
