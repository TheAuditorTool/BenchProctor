# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io


async def BenchmarkTest30688(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
