# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest24425(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    request.session['user'] = str(data)
    return {"updated": True}
