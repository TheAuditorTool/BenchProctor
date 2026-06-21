# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13368(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
