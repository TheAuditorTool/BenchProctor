# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html


def to_text(value):
    return str(value).strip()

async def BenchmarkTest15968(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return {"updated": True}
