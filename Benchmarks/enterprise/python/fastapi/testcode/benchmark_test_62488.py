# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62488(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    eval(str(data))
    return {"updated": True}
