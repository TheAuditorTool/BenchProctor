# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest08053(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
