# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00430(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    os.remove(str(data))
    return {"updated": True}
