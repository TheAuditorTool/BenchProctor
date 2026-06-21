# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest09026(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
