# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest37498(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
