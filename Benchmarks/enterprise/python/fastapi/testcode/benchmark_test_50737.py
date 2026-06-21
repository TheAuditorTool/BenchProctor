# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest50737(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    result = 100 / int(str(data))
    return {"updated": True}
