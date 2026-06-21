# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest50807(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
