# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01058(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
