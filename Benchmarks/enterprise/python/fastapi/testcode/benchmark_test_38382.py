# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38382(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    request.session['data'] = str(data)
    return {"updated": True}
