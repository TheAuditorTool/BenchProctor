# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32577(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
