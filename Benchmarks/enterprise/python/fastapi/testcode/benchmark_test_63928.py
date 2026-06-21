# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import tempfile


async def BenchmarkTest63928(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
