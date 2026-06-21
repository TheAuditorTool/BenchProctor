# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest05292(request: Request):
    referer_value = request.headers.get('referer', '')
    os.system('echo ' + str(referer_value))
    return {"updated": True}
