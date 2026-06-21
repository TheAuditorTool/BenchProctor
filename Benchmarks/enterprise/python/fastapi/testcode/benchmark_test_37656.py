# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest37656(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
