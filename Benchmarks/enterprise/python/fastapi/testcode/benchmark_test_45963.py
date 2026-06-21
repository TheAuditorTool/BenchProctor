# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest45963(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
