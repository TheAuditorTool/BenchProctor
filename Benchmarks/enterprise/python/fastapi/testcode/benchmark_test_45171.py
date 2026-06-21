# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45171(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
