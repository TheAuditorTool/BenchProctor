# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest07009(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    globals()['counter'] = int(data)
    return {"updated": True}
