# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest41337(request: Request):
    host_value = request.headers.get('host', '')
    with open('/var/uploads/' + str(host_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
