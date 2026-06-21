# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04511(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    request.session['data'] = str(data)
    return {"updated": True}
