# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest48917(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
