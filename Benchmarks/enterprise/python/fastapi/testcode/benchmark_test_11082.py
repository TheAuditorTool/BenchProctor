# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest11082(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
