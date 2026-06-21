# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os
import ast


async def BenchmarkTest18453(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
