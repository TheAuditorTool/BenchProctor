# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69243(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
