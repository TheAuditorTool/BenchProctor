# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68433(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
