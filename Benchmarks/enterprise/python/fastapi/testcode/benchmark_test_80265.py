# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest80265(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    os.remove(str(data))
    return {"updated": True}
