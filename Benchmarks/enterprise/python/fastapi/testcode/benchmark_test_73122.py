# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73122(request: Request):
    auth_header = request.headers.get('authorization', '')
    os.remove(str(auth_header))
    return {"updated": True}
