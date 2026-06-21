# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest31998(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
