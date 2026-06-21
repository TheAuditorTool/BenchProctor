# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00184(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
