# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest71245(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    auth_check('user', forwarded_ip)
    return {"updated": True}
