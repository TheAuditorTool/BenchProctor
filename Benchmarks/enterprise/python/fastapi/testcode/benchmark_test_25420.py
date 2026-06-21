# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import tempfile


async def BenchmarkTest25420(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
