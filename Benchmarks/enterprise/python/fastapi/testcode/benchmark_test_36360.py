# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest36360(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    json.loads(data)
    return {"updated": True}
