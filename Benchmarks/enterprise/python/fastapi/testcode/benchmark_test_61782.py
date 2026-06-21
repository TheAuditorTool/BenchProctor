# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest61782(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    os.system('echo ' + str(data))
    return {"updated": True}
