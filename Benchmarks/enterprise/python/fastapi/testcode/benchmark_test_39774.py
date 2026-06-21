# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest39774(request: Request, field: str = Form('')):
    field_value = field
    with open('/var/app/data/' + str(field_value), 'r') as fh:
        content = fh.read()
    return content
