# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests
import pickle


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02725(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = FormData(payload=api_value).payload
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
