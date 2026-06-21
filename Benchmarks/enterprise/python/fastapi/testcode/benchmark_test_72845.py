# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import pickle


async def BenchmarkTest72845(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
