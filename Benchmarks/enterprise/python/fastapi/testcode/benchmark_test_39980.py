# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39980(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
