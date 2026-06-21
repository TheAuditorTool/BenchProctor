# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest04038(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
