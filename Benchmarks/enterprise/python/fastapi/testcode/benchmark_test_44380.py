# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest44380(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
