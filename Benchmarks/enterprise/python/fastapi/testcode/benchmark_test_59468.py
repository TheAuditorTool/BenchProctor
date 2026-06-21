# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest59468(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    globals()['counter'] = int(data)
    return {"updated": True}
