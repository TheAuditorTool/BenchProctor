# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest71604(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    os.remove(str(data))
    return {"updated": True}
