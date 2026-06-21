# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest60546(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    json.loads(data)
    return {"updated": True}
