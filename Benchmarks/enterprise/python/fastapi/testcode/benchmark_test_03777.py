# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03777(request: Request):
    upload_name = (await request.form()).get('upload', '')
    with open('/var/app/data/' + str(upload_name), 'r') as fh:
        content = fh.read()
    return content
