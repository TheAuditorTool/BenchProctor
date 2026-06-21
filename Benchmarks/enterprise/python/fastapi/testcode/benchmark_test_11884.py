# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11884(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
