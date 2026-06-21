# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest05046(request: Request):
    path_value = request.path_params.get('id', '')
    with open('/var/uploads/' + str(path_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
