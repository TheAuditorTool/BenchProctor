# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11846(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
