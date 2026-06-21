# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57607(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
