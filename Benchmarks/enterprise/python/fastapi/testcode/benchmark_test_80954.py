# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80954(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
