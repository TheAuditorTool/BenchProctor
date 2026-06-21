# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest74121():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
