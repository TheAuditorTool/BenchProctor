# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest80116(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    _resp = requests.get(str(forwarded_ip))
    exec(_resp.text)
    return {"updated": True}
