# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest65685(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
