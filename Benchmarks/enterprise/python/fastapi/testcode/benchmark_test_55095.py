# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest55095(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    request.session['user'] = str(data)
    return {"updated": True}
