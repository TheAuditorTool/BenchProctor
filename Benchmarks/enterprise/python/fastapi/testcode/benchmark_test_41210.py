# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41210(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
