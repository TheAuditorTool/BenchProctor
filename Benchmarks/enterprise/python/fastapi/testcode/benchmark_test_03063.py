# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import time


async def BenchmarkTest03063(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
