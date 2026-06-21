# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest29186(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    os.remove(str(data))
    return {"updated": True}
