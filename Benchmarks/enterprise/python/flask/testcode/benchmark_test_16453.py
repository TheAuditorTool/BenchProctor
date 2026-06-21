# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import requests


def BenchmarkTest16453():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = api_value if api_value else 'default'
    return redirect(str(data))
