# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39773(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    result = 100 / int(str(data))
    return {"updated": True}
