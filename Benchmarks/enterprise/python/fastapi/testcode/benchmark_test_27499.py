# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
import tempfile


async def BenchmarkTest27499(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
