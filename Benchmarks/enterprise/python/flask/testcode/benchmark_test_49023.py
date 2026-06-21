# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import socket


def BenchmarkTest49023():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    prefix = ''
    data = prefix + str(api_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
