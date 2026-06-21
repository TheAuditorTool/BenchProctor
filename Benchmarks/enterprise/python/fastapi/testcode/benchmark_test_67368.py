# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67368(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    os.chmod('/var/app/data/' + str(forwarded_ip), 0o777)
    return {"updated": True}
