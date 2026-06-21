# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import pickle


async def BenchmarkTest80043(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    pending = list(str(api_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
