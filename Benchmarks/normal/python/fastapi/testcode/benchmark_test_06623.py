# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest06623(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
