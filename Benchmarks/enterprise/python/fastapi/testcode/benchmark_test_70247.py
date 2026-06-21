# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70247(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
