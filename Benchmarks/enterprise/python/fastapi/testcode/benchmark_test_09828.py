# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09828(request: Request):
    stdin_value = input('input: ')
    with open('/var/app/data/' + str(stdin_value), 'w') as fh:
        fh.write('data')
    return {"updated": True}
