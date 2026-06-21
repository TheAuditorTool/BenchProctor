# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest34841(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
