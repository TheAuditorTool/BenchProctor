# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33163(request: Request):
    referer_value = request.headers.get('referer', '')
    request.session['data'] = str(referer_value)
    return {"updated": True}
