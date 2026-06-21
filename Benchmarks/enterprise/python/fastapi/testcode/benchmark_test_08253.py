# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest08253(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    os.remove(str(data))
    return {"updated": True}
