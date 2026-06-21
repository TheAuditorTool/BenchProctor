# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09870(request: Request):
    auth_header = request.headers.get('authorization', '')
    int(str(auth_header))
    return {"updated": True}
