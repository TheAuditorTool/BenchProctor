# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest12172(request: Request):
    upload_name = (await request.form()).get('upload', '')
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
