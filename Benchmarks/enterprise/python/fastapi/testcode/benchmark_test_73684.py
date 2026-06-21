# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import subprocess


async def BenchmarkTest73684(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
