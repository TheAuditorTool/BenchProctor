# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76357(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
