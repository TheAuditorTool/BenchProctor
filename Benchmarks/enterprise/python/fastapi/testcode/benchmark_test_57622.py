# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest57622(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    os.remove(str(data))
    return {"updated": True}
