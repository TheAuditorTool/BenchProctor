# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest42265(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
