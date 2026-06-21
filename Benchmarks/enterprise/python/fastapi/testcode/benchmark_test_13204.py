# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13204(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
