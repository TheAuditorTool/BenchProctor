# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest69014(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
