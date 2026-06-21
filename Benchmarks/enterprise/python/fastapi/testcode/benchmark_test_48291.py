# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest48291(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    os.system('echo ' + str(data))
    return {"updated": True}
