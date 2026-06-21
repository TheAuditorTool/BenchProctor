# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest25670(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
