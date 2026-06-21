# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast


async def BenchmarkTest69732(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
