# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70410(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
