# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest01508(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    globals()['counter'] = int(data)
    return {"updated": True}
