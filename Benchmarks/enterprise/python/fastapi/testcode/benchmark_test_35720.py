# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest35720(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
