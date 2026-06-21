# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest44481(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
