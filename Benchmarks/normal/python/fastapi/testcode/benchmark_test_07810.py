# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest07810(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
