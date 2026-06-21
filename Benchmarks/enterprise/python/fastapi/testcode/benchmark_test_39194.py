# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39194(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(multipart_value))
    return {"updated": True}
