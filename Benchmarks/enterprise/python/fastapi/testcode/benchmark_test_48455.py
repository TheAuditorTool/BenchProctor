# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest48455(request: Request):
    origin_value = request.headers.get('origin', '')
    os.remove(str(origin_value))
    return {"updated": True}
