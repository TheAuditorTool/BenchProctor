# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest78734(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
