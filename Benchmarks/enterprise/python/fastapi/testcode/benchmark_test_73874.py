# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73874(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
