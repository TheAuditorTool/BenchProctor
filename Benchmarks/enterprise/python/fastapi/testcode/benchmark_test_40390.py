# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40390(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
