# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest79548(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    globals()['counter'] = int(data)
    return {"updated": True}
