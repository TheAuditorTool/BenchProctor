# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest28118(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
