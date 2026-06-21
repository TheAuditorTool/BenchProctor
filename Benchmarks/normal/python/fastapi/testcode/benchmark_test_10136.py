# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10136(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
