# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72377(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
