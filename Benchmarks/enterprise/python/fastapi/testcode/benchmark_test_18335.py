# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import pickle


async def BenchmarkTest18335(request: Request, field: str = Form('')):
    field_value = field
    prefix = ''
    data = prefix + str(field_value)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
