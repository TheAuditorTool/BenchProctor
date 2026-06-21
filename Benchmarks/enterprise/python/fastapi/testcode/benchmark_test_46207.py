# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest46207(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = coalesce_blank(upload_name)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
