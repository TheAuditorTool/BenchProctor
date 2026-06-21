# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79538(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    request.session['data'] = str(data)
    return {"updated": True}
