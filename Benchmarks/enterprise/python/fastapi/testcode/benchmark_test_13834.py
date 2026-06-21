# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13834(request: Request):
    user_id = request.query_params.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
