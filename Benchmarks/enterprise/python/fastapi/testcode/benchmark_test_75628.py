# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest75628(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    os.remove(str(data))
    return {"updated": True}
