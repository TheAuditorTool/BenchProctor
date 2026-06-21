# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest06518(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
