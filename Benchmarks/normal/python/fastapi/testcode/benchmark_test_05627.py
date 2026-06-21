# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05627(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
