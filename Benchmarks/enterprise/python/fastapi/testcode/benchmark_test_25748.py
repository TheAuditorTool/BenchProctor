# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest25748(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
