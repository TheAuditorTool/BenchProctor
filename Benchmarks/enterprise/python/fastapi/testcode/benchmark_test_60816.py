# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest60816(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    os.remove(str(data))
    return {"updated": True}
