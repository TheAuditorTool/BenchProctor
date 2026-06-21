# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38689(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
