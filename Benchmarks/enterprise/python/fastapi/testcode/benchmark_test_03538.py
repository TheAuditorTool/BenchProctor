# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest03538(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
