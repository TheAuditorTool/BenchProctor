# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io


async def BenchmarkTest70821(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
