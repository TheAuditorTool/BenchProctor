# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47439(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
