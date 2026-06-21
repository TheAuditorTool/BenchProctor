# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os


async def BenchmarkTest31815(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
