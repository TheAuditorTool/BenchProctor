# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67028(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
