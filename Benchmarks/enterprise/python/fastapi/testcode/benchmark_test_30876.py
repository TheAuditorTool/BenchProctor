# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest30876(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
