# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


async def BenchmarkTest33407(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    globals()['counter'] = int(data)
    return {"updated": True}
