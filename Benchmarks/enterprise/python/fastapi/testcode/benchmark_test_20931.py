# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest20931(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    auth_check('user', data)
    return {"updated": True}
