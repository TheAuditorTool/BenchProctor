# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07038(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
