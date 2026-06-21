# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest53780(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = to_text(forwarded_ip)
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return {"updated": True}
