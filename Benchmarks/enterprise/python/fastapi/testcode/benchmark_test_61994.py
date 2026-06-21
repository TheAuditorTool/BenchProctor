# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest61994(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
