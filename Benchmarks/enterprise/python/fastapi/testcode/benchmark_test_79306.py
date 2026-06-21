# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest79306(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
