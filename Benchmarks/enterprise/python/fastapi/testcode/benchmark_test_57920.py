# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57920(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
