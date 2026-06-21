# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest51928(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    int(str(data))
    return {"updated": True}
