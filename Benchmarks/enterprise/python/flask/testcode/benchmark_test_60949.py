# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest60949():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
