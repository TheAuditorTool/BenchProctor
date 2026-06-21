# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest06103(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
