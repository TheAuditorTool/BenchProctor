# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78520(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
