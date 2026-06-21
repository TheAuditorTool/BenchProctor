# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import socket


async def BenchmarkTest53986(request: Request, field: str = Form('')):
    field_value = field
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
