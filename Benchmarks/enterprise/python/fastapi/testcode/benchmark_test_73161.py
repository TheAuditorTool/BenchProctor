# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest73161(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    eval(str(data))
    return {"updated": True}
