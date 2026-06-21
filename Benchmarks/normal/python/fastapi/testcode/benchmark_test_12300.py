# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12300(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
