# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest58523(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
