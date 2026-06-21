# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11761(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    request.session['data'] = str(data)
    return {"updated": True}
