# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest00648(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
