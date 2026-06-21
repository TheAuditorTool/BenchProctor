# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68743(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    request.session['user'] = str(data)
    return {"updated": True}
