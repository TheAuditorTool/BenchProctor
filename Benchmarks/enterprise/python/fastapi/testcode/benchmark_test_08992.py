# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest08992(request: Request, field: str = Form('')):
    field_value = field
    prefix = ''
    data = prefix + str(field_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
