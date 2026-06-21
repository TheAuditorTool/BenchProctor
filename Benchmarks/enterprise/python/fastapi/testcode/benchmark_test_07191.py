# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest07191(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
