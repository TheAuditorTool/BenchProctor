# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import requests


async def BenchmarkTest76953(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
