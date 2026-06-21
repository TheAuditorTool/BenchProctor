# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60908(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    with open('/var/app/data/' + str(multipart_value), 'r') as fh:
        content = fh.read()
    return content
