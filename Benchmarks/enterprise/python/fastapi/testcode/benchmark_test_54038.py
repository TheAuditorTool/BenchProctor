# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest54038(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    os.remove(str(data))
    return {"updated": True}
