# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest77288(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    return HTMLResponse('<script src="' + str(data) + '"></script>')
