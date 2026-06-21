# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05920(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    result = 100 / int(str(data))
    return {"updated": True}
