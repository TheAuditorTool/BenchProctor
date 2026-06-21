# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest78988(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    request.session['data'] = str(data)
    return {"updated": True}
