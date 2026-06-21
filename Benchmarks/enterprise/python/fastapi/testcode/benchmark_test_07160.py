# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07160(request: Request):
    upload_name = request.query_params.get('filename', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
