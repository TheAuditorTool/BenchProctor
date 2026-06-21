# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest63833(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    os.remove(str(data))
    return {"updated": True}
