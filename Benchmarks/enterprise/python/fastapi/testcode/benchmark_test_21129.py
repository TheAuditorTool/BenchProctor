# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21129(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    request.session['user'] = str(data)
    return {"updated": True}
