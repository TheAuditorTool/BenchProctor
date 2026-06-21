# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest10391(request: Request):
    user_id = request.query_params.get('id', '')
    data = default_blank(user_id)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
