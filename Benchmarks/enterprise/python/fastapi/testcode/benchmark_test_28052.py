# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest28052(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
