# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest41802(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
