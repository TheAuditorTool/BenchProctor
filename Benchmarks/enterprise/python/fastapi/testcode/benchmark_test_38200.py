# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest38200(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
