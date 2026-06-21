# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest73737(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    json.loads(data)
    return {"updated": True}
