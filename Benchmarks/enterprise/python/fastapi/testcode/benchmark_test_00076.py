# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


def relay_value(value):
    return value

async def BenchmarkTest00076(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return {"updated": True}
