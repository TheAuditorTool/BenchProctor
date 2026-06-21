# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest76196(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    os.remove(str(data))
    return {"updated": True}
