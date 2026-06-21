# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79033(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
