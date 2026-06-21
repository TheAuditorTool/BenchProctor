# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest42388(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    os.remove(str(forwarded_ip))
    return {"updated": True}
