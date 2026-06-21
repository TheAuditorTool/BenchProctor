# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest46208(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
