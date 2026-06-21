# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def normalise_input(value):
    return value.strip()

async def BenchmarkTest30426(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
