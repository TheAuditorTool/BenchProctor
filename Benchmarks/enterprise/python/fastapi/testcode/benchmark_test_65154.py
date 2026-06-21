# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import requests


async def BenchmarkTest65154(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    def normalize(value):
        return value.strip()
    data = normalize(api_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
