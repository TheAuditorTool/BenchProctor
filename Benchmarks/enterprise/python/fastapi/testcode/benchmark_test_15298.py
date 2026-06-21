# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest15298(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
