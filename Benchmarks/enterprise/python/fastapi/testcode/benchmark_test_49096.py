# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest49096(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    os.remove(str(data))
    return {"updated": True}
