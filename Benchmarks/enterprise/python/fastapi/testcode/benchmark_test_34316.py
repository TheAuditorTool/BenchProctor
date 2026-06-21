# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest34316(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
