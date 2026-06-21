# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os
import time
import ast


async def BenchmarkTest03762(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
