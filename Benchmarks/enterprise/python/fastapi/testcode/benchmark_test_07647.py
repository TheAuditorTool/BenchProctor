# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from fastapi import Form


async def BenchmarkTest07647(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
