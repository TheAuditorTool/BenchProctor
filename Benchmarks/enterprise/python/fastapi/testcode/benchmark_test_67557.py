# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67557(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    request.session['data'] = str(data)
    return {"updated": True}
