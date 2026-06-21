# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import socket


async def BenchmarkTest16559(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
