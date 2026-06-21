# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


request_state: dict[str, str] = {}

async def BenchmarkTest45142(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return {"updated": True}
