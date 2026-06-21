# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest28033(request: Request):
    upload_name = request.query_params.get('filename', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
