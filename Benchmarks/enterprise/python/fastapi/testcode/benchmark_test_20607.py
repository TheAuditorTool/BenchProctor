# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64
from starlette.responses import HTMLResponse


async def BenchmarkTest20607(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return HTMLResponse('<script src="' + str(data) + '"></script>')
