# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest37388(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
