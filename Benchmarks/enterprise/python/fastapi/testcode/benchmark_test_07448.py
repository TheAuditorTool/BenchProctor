# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest07448(request: Request, field: str = Form('')):
    field_value = field
    with open('/var/uploads/' + str(field_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
