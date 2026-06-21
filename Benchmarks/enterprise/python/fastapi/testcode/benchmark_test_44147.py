# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44147(request: Request):
    upload_name = request.query_params.get('filename', '')
    data = ' '.join(str(upload_name).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
