# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest19916(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    globals()['counter'] = int(data)
    return {"updated": True}
