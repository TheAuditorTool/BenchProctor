# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest65364(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    auth_check('user', hashlib.sha256(str(forwarded_ip).encode()).hexdigest())
    return {"updated": True}
