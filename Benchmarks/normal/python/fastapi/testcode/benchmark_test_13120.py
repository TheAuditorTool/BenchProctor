# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest13120(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
