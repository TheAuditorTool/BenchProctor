# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest03293(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    os.system('echo ' + str(data))
    return {"updated": True}
