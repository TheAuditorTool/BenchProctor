# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest80067(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    globals()['counter'] = int(data)
    return {"updated": True}
