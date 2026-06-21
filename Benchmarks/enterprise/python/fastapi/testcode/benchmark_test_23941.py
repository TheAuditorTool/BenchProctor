# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest23941(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
