# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest64152(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    request.session['user'] = str(data)
    return {"updated": True}
