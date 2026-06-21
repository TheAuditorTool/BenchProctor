# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from urllib.parse import unquote


async def BenchmarkTest48411(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    globals()['counter'] = int(data)
    return {"updated": True}
