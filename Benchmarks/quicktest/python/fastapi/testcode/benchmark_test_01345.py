# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest01345(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    os.system('echo ' + str(data))
    return {"updated": True}
