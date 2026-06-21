# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest46521(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    json.loads(data)
    return {"updated": True}
