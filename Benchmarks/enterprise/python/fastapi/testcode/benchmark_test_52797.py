# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest52797(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
