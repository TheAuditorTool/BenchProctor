# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import socket


async def BenchmarkTest06849(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
