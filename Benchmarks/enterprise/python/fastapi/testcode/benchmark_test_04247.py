# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04247(request: Request):
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
