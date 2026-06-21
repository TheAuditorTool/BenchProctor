# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest51759(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    os.remove(str(data))
    return {"updated": True}
