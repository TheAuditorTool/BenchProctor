# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest01688(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
