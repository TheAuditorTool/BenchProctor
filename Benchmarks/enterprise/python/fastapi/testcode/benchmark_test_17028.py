# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest17028(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
