# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest05976(request: Request):
    origin_value = request.headers.get('origin', '')
    data = normalise_input(origin_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
