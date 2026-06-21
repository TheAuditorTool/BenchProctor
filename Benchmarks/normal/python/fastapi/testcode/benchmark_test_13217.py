# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13217(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
