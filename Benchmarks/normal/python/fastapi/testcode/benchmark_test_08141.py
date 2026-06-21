# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08141(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
