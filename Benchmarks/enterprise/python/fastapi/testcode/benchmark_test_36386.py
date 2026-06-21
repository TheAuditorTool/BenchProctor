# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest36386(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
