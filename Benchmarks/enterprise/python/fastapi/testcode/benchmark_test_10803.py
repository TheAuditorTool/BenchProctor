# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10803(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
