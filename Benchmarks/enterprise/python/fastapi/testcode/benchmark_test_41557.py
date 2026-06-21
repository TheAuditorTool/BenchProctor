# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest41557(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
