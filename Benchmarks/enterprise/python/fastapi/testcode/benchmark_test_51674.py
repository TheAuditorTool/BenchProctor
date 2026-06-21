# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest51674(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    os.remove(str(data))
    return {"updated": True}
