# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest51339(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return {"updated": True}
