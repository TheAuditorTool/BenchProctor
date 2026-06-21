# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


def to_text(value):
    return str(value).strip()

async def BenchmarkTest50480(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = to_text(forwarded_ip)
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
