# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest08901(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
