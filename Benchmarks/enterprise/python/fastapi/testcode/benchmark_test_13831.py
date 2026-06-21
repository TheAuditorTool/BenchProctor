# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest13831(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    exec(str(data))
    return {"updated": True}
