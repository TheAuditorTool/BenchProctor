# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68695(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    int(str(data))
    return {"updated": True}
