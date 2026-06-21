# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest09461(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
