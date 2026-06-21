# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest58618(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    eval(str(data))
    return {"updated": True}
