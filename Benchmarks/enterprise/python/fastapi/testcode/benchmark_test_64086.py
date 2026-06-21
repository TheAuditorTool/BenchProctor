# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64086(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    request.session['data'] = str(data)
    return {"updated": True}
