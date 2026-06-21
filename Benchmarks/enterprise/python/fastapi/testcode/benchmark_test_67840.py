# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67840(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
