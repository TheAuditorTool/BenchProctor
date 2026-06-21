# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import os


async def BenchmarkTest53108(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
