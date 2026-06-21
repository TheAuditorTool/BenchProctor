# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest39842(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
