# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest75863(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
