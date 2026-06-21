# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os


async def BenchmarkTest64286(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
