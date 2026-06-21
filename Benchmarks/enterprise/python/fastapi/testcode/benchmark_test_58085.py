# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest58085(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    os.remove(str(data))
    return {"updated": True}
