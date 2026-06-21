# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest15384(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    globals()['counter'] = int(header_value)
    return {"updated": True}
