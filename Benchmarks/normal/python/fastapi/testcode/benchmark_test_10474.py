# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest10474(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return {"updated": True}
