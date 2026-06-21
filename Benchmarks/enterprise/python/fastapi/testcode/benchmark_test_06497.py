# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest06497(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    os.remove(str(data))
    return {"updated": True}
