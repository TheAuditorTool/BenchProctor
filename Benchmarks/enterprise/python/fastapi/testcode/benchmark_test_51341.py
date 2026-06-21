# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest51341(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    os.remove(str(data))
    return {"updated": True}
