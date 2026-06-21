# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03045(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(forwarded_ip))
    return {"updated": True}
