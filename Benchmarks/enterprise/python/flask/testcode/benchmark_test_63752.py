# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest63752():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return jsonify({"result": "success"})
