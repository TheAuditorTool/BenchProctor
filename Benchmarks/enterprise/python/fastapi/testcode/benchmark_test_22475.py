# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest22475(request: Request):
    user_id = request.query_params.get('id', '')
    os.remove(str(user_id))
    return {"updated": True}
