# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54901(request: Request):
    path_value = request.path_params.get('id', '')
    with open('/var/app/data/' + str(path_value), 'r') as fh:
        content = fh.read()
    return content
