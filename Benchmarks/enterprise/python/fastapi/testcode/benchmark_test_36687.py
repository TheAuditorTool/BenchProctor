# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest36687(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
