# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest80105(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    importlib.import_module(str(data))
    return {"updated": True}
