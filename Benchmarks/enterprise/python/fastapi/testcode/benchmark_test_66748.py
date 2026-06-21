# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest66748(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
