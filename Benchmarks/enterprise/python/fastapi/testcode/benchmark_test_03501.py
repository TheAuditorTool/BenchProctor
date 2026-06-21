# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest03501(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
