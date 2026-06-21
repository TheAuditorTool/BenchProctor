# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60085(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
