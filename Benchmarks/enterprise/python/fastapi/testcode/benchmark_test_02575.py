# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02575(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    request.session['user'] = str(data)
    return {"updated": True}
