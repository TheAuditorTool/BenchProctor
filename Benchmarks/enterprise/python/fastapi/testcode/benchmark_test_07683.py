# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07683(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
