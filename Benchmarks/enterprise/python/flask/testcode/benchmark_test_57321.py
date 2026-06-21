# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest57321():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
