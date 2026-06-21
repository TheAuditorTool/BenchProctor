# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest72752(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    os.remove(str(data))
    return {"updated": True}
