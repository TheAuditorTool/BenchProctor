# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import requests


def BenchmarkTest00673():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return redirect(str(data))
