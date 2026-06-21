# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import importlib
import sys


async def BenchmarkTest77677(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
