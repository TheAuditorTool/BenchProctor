# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75156(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
