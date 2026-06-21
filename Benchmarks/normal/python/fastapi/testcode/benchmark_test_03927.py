# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest03927(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
