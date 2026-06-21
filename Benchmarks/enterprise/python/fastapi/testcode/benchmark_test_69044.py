# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69044(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
