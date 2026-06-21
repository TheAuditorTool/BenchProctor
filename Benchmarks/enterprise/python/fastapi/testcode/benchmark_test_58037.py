# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58037(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
