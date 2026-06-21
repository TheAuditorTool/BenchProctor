# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest64049(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
