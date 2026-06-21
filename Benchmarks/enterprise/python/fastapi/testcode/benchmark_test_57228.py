# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest57228(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
