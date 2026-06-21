# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest22487(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    os.remove(str(data))
    return {"updated": True}
