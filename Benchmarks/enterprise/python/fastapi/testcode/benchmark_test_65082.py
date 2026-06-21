# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest65082(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    os.remove(str(data))
    return {"updated": True}
