# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73877(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    os.remove(str(data))
    return {"updated": True}
