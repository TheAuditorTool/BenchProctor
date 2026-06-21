# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


async def BenchmarkTest51444(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    globals()['counter'] = int(data)
    return {"updated": True}
