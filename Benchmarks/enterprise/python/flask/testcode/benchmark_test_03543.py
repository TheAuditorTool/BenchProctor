# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest03543():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
