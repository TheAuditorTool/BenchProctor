# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05065(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
