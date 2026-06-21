# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest53277(request: Request, field: str = Form('')):
    field_value = field
    os.chmod('/var/app/data/' + str(field_value), 0o777)
    return {"updated": True}
