# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest12052(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
