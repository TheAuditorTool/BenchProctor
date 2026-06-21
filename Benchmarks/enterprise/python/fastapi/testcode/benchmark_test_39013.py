# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest39013(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return {"updated": True}
