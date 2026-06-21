# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import time


async def BenchmarkTest06973(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
