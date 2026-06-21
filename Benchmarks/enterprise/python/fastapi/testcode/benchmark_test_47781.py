# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest47781(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
