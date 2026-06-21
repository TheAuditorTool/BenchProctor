# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest72659(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    importlib.import_module(str(data))
    return {"updated": True}
