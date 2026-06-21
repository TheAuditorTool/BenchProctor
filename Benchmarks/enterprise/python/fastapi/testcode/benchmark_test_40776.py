# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40776(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    request.session['data'] = str(data)
    return {"updated": True}
