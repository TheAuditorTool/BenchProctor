# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01808(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
