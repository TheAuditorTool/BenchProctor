# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19222(request: Request):
    auth_header = request.headers.get('authorization', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(auth_header))
    return {"updated": True}
