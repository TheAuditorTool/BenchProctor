# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02043(request: Request):
    user_id = request.query_params.get('id', '')
    with open(os.path.join('/var/app/data', str(user_id)), 'r') as fh:
        content = fh.read()
    return content
