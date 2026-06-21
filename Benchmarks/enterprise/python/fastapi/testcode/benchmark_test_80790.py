# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80790(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    eval(str(data))
    return {"updated": True}
