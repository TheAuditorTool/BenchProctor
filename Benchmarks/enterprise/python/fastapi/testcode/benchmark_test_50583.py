# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest50583(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
