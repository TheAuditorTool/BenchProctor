# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13900(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
