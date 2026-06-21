# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest36523(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    importlib.import_module(str(data))
    return {"updated": True}
