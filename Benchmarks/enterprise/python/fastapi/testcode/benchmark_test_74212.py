# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest74212(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
