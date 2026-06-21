# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest80654(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
