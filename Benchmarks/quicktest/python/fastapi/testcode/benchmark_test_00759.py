# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00759(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
