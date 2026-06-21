# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest50907(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
