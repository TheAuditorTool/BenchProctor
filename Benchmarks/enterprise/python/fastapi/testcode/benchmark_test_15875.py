# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15875(request: Request):
    referer_value = request.headers.get('referer', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(referer_value))
    return {"updated": True}
