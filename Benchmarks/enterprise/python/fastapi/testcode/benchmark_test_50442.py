# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


def normalise_input(value):
    return value.strip()

async def BenchmarkTest50442(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = normalise_input(multipart_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
