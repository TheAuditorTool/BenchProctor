# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest27910(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    importlib.import_module(str(data))
    return {"updated": True}
