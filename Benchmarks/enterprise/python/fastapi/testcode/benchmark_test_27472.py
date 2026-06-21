# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from urllib.parse import unquote


async def BenchmarkTest27472(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
