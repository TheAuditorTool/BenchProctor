# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11515(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not str(forwarded_ip).isdigit():
        raise ValueError('invalid input: ' + str(forwarded_ip))
    return {"updated": True}
