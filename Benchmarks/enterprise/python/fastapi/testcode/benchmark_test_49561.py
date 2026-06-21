# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49561(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
