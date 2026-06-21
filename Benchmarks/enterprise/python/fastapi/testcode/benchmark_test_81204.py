# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest81204(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
