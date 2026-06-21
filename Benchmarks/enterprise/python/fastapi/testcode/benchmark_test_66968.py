# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest66968(request: Request):
    user_id = request.query_params.get('id', '')
    os.chmod('/var/app/data/' + str(user_id), 0o777)
    return {"updated": True}
