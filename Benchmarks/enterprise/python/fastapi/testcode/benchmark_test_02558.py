# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02558(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    os.remove(str(data))
    return {"updated": True}
