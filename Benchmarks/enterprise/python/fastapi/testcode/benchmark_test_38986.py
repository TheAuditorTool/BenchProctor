# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38986(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
