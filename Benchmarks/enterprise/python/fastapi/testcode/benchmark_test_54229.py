# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import os


async def BenchmarkTest54229(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
