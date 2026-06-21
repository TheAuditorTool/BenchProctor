# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest29494(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    globals()['counter'] = int(data)
    return {"updated": True}
