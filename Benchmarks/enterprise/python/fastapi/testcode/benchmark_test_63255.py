# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63255(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
