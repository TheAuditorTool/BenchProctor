# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08160(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
