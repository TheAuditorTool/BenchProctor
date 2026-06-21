# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest75201(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
