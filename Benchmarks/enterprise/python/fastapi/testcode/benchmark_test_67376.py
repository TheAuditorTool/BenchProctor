# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67376(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    os.remove(str(data))
    return {"updated": True}
