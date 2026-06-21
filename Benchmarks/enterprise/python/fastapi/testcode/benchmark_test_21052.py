# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21052(request: Request):
    ua_value = request.headers.get('user-agent', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(ua_value))
    return {"updated": True}
