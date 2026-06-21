# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26807(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
