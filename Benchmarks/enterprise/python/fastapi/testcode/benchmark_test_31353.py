# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest31353(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
