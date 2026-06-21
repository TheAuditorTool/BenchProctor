# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17716(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    request.session['data'] = str(data)
    return {"updated": True}
