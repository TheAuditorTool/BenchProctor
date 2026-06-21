# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07053(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
