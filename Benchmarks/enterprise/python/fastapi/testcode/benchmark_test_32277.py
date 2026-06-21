# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest32277(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    json.loads(data)
    return {"updated": True}
