# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import importlib
import sys


async def BenchmarkTest69140(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
