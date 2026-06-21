# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest04684(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    json.loads(data)
    return {"updated": True}
