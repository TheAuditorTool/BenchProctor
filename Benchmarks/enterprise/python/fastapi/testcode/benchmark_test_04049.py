# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest04049(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return {"updated": True}
