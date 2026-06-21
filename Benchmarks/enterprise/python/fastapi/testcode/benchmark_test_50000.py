# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest50000(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
