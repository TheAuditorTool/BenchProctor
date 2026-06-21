# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14456(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
