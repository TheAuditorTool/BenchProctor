# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02924(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    os.remove(str(data))
    return {"updated": True}
