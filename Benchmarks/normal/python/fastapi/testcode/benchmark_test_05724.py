# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05724(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
