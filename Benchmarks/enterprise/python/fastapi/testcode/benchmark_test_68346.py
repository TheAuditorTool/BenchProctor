# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68346(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    request.session['data'] = str(data)
    return {"updated": True}
