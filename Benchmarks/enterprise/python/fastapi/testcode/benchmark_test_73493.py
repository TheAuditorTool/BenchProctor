# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest73493(request: Request):
    user_id = request.query_params.get('id', '')
    sys.path.insert(0, str(user_id))
    importlib.import_module('report_renderer')
    return {"updated": True}
