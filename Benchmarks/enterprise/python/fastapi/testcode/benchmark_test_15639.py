# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests
import pickle


async def BenchmarkTest15639(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = json.loads(api_value).get('value', '')
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
