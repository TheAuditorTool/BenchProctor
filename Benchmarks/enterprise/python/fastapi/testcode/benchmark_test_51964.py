# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51964(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    result = 100 / int(str(data))
    return {"updated": True}
