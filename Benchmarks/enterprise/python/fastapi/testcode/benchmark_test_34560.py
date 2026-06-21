# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest34560(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
