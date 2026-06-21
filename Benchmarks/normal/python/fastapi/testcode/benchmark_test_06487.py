# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import socket


async def BenchmarkTest06487(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    prefix = ''
    data = prefix + str(api_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
