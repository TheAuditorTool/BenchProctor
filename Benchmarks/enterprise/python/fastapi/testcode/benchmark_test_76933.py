# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest76933(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
