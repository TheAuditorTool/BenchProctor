# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37970(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    request.session['data'] = str(data)
    return {"updated": True}
