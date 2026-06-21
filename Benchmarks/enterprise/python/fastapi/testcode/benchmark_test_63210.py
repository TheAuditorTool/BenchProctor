# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63210(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
