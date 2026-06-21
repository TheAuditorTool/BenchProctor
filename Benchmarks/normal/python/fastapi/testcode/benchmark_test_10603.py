# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest10603(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    globals()['counter'] = int(data)
    return {"updated": True}
