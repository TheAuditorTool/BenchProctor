# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40668(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    request.session['data'] = str(data)
    return {"updated": True}
