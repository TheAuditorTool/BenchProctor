# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47510(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
