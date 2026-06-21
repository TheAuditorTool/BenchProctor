# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest52325(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    os.remove(str(data))
    return {"updated": True}
