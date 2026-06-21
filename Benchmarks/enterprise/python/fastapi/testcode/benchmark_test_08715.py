# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


request_state: dict[str, str] = {}

async def BenchmarkTest08715(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
