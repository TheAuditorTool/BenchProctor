# SPDX-License-Identifier: Apache-2.0
import os
import requests
from flask import jsonify


def BenchmarkTest73337():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    parts = str(api_value).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
