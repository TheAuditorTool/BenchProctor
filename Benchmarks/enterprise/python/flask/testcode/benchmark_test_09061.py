# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest09061():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
