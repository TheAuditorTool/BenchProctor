# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest23456(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
