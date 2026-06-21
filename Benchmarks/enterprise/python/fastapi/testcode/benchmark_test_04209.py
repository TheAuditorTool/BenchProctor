# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest04209(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
