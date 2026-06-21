# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest01311(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    importlib.import_module(str(data))
    return {"updated": True}
