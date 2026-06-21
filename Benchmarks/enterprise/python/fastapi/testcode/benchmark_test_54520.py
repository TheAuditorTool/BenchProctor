# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest54520(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
