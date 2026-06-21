# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest34164(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    int(str(data))
    return {"updated": True}
