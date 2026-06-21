# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import pickle


async def BenchmarkTest05534(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
