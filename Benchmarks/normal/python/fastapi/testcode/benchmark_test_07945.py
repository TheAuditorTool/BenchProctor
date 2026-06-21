# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07945(request: Request):
    upload_name = request.query_params.get('filename', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
