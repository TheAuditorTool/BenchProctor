# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest00519(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(env_value) + ' -->')
