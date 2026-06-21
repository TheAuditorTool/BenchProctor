# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest64317(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    importlib.import_module(str(data))
    return {"updated": True}
