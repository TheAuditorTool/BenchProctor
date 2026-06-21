# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest79885(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    os.remove(str(data))
    return {"updated": True}
