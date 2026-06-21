# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest20985():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
