# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest23714(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
