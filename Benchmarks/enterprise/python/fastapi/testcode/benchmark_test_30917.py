# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io


async def BenchmarkTest30917(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
