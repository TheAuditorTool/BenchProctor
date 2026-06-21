# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest00729(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
