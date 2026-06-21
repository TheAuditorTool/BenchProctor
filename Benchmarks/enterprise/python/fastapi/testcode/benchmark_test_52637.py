# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest52637(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
