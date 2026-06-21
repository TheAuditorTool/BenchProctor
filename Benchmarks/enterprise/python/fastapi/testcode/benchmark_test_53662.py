# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest53662(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    os.system('echo ' + str(data))
    return {"updated": True}
