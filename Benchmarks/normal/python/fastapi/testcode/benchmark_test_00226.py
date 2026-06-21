# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import socket


async def BenchmarkTest00226(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
