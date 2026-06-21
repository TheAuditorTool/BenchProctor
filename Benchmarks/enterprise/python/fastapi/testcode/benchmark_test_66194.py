# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest66194(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
