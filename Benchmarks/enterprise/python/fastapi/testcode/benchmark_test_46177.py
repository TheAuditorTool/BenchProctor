# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest46177(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
