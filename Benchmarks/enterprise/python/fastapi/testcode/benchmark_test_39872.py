# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


request_state: dict[str, str] = {}

async def BenchmarkTest39872(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
