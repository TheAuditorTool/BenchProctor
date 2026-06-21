# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61516(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
