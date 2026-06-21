# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest73505(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
