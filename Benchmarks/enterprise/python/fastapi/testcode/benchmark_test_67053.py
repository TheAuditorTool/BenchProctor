# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67053(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
