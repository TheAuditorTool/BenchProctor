# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest61953(request: Request):
    ua_value = request.headers.get('user-agent', '')
    os.remove(str(ua_value))
    return {"updated": True}
