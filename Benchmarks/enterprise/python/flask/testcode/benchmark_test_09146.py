# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest09146():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
