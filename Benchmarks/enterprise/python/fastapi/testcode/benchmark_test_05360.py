# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest05360(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    globals()['counter'] = int(data)
    return {"updated": True}
