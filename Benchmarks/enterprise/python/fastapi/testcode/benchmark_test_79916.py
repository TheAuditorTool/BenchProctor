# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest79916(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    os.system('echo ' + str(data))
    return {"updated": True}
