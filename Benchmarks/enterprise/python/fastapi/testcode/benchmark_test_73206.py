# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73206(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    os.remove(str(data))
    return {"updated": True}
