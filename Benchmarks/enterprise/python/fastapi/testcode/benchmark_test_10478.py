# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest10478(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
