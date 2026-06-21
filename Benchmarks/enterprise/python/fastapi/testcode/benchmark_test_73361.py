# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73361(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    os.system('echo ' + str(data))
    return {"updated": True}
