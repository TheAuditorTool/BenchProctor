# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01246(request: Request):
    auth_header = request.headers.get('authorization', '')
    exec(str(auth_header))
    return {"updated": True}
