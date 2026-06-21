# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57146(request: Request):
    upload_name = request.query_params.get('filename', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
