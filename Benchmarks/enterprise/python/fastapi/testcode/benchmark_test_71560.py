# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71560(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    eval(str(data))
    return {"updated": True}
