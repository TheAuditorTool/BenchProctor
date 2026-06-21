# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import tempfile


async def BenchmarkTest73024(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
