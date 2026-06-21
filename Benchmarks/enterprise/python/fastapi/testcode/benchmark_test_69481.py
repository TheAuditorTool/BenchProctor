# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest69481(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
