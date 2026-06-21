# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39962(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    os.unlink('/var/app/data/' + str(forwarded_ip))
    return {"updated": True}
