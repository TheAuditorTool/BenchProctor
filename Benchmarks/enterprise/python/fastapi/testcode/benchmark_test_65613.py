# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


request_state: dict[str, str] = {}

async def BenchmarkTest65613(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return {"updated": True}
