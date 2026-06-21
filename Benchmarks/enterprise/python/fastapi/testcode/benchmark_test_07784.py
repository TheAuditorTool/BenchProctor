# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


async def BenchmarkTest07784(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    globals()['counter'] = int(data)
    return {"updated": True}
