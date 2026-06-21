# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest17664(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    os.remove(str(cookie_value))
    return {"updated": True}
