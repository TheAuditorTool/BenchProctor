# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76894(request: Request):
    upload_name = request.query_params.get('filename', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
