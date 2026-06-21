# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest65592(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
