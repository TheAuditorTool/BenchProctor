# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest45477(request: Request):
    path_value = request.path_params.get('id', '')
    sys.path.insert(0, str(path_value))
    importlib.import_module('report_renderer')
    return {"updated": True}
