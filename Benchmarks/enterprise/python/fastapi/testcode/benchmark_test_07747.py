# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07747(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
