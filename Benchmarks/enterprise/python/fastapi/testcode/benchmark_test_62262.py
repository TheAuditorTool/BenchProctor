# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest62262(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
