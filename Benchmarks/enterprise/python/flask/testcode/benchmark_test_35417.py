# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest35417():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    auth_check('user', data)
    return jsonify({"result": "success"})
