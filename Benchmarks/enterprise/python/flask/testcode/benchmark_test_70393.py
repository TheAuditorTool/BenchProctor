# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest70393():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
