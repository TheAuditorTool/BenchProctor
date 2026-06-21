# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54544(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    request.session['user'] = str(data)
    return {"updated": True}
