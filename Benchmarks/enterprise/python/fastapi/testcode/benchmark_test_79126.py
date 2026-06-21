# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79126(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    eval(str(data))
    return {"updated": True}
