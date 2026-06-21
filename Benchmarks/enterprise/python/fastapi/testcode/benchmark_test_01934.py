# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os


async def BenchmarkTest01934(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    return HTMLResponse('<div>' + str(env_value) + '</div>')
