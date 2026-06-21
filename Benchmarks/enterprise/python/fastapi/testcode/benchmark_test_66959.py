# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66959(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
