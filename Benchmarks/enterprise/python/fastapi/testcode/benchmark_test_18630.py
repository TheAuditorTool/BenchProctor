# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest18630(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    os.remove(str(data))
    return {"updated": True}
