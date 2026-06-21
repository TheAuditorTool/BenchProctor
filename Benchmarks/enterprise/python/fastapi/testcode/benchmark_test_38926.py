# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest38926(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
