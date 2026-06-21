# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import requests


def BenchmarkTest20703():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = (lambda v: v.strip())(api_value)
    return redirect(str(data))
