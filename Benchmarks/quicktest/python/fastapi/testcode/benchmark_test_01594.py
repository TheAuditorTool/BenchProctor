# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest01594(request: Request):
    referer_value = request.headers.get('referer', '')
    reader = make_reader(referer_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
