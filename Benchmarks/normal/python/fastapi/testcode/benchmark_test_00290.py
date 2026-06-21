# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00290(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
