# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest35612():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
