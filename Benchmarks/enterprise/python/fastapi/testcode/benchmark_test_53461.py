# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53461(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    exec(str(data))
    return {"updated": True}
