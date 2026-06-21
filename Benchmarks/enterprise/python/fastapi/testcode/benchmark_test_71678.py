# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest71678(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
