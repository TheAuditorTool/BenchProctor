# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest03915(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    os.remove(str(data))
    return {"updated": True}
