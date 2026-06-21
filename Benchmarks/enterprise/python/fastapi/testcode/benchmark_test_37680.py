# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37680(request: Request):
    auth_header = request.headers.get('authorization', '')
    eval(str(auth_header))
    return {"updated": True}
