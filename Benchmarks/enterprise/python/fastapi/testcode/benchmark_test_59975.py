# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest59975(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
