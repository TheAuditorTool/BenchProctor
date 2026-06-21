# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest56997(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    os.remove(str(data))
    return {"updated": True}
