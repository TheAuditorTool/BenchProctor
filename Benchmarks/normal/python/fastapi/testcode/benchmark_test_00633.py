# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest00633(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    globals()['counter'] = int(data)
    return {"updated": True}
