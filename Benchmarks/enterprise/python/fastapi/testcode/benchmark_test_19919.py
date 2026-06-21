# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest19919(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
