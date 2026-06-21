# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest45401(request: Request):
    path_value = request.path_params.get('id', '')
    globals()['counter'] = int(path_value)
    return {"updated": True}
