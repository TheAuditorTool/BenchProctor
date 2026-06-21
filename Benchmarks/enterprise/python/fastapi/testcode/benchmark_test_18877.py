# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18877(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
