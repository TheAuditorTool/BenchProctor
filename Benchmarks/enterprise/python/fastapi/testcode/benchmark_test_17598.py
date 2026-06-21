# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17598(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
