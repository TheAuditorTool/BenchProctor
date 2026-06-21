# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest22778(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
