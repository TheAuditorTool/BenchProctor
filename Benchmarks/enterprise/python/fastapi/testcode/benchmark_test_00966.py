# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00966(request: Request):
    stdin_value = input('input: ')
    data = ' '.join(str(stdin_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
