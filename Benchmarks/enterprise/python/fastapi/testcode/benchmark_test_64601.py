# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64601(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    request.session['user'] = str(data)
    return {"updated": True}
