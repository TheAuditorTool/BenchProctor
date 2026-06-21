# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57788(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    eval(str(data))
    return {"updated": True}
