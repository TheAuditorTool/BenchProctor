# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def relay_value(value):
    return value

async def BenchmarkTest01846(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return {"updated": True}
