# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest38880(request: Request):
    user_id = request.query_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return {"updated": True}
