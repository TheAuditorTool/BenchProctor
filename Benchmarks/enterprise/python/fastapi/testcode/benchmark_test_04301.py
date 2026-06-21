# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest04301(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
