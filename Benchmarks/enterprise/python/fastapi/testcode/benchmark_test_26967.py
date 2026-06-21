# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26967(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
