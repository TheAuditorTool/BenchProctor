# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest25572(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
