# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest47434(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    request.session['data'] = str(data)
    return {"updated": True}
