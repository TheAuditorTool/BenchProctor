# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24248(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
