# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56016(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    eval(str(data))
    return {"updated": True}
