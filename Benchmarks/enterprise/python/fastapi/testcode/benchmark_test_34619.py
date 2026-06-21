# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest34619(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
