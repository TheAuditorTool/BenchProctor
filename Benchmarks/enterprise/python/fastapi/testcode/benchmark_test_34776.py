# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import csv
import io
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest34776(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return {"updated": True}
