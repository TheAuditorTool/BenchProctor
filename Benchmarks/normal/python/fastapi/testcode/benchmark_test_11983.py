# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11983(request: Request):
    upload_name = (await request.form()).get('upload', '')
    with open('/var/uploads/' + str(upload_name), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
