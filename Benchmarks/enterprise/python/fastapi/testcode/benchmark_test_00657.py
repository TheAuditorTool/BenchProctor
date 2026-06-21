# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00657(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
