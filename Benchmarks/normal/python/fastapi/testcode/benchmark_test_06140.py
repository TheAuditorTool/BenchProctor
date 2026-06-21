# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest06140(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
