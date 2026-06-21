# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69067(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    eval(str(forwarded_ip))
    return {"updated": True}
