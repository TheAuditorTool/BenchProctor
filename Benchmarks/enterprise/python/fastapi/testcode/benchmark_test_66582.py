# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66582(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
