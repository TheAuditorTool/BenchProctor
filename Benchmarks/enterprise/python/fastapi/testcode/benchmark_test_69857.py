# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest69857(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
