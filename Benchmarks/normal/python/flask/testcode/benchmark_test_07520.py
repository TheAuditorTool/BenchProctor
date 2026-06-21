# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest07520():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.normpath(data)
    with open('/var/uploads/' + str(checked_path), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
