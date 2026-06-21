# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest45183(request: Request):
    upload_name = request.query_params.get('filename', '')
    with open('/var/uploads/' + str(upload_name), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
