# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest05822(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    json.loads(data)
    return {"updated": True}
