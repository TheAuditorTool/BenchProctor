# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest26691(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
