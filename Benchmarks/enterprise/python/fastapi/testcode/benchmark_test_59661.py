# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest59661(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    os.remove(str(data))
    return {"updated": True}
