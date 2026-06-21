# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest24882(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    result = 100 / int(str(data))
    return {"updated": True}
