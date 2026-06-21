# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import tempfile


async def BenchmarkTest08086(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
