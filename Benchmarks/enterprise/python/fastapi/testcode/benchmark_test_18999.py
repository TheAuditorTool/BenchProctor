# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import time


async def BenchmarkTest18999(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
