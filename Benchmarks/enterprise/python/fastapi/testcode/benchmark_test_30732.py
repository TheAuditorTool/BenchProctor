# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30732(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    int(str(data))
    return {"updated": True}
