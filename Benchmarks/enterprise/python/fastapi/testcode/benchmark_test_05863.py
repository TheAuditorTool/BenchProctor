# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest05863(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    os.seteuid(65534)
    return {"updated": True}
