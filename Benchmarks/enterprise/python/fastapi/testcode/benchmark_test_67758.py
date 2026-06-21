# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest67758(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    importlib.import_module(str(data))
    return {"updated": True}
