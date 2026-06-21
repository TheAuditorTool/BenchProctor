# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest73209(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    importlib.import_module(str(data))
    return {"updated": True}
