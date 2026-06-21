# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest21024(request: Request):
    user_id = request.query_params.get('id', '')
    os.system('echo ' + str(user_id))
    return {"updated": True}
