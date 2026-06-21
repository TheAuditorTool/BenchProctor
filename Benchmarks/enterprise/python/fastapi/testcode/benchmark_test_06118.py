# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest06118(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    return HTMLResponse('<script src="' + str(data) + '"></script>')
