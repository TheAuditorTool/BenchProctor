# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os


async def BenchmarkTest19474(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
