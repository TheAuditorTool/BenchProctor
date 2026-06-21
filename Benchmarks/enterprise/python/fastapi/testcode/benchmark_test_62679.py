# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest62679(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
