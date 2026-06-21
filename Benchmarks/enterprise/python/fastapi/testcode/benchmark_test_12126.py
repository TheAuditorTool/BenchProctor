# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest12126(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
