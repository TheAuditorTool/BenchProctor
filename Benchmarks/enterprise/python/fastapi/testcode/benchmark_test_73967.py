# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73967(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    os.remove(str(data))
    return {"updated": True}
